import sys
import os
import pandas as pd

# Adiciona o diretório raiz do projeto ao sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from sqlalchemy.orm import Session
from api.core.database import SessionLocal, engine
from api.models.base import Mantenedora, Instituicao, Base

def load_data():
    Base.metadata.create_all(bind=engine)
    
    db: Session = SessionLocal()

    try:
        # --- CORREÇÃO 1: CRIAR MANTENEDORA PADRÃO ---
        # Como o CSV não tem a mantenedora, criamos uma para associar a todas as IES.
        nome_mantenedora_padrao = "Mantenedora Padrão (Dados não disponíveis no CSV)"
        mantenedora_padrao = db.query(Mantenedora).filter(Mantenedora.nome == nome_mantenedora_padrao).first()
        if not mantenedora_padrao:
            mantenedora_padrao = Mantenedora(nome=nome_mantenedora_padrao)
            db.add(mantenedora_padrao)
            db.commit()
            db.refresh(mantenedora_padrao)
        
        mantenedora_id_padrao = mantenedora_padrao.id
        
        print("Lendo o arquivo CSV...")
        csv_path = os.path.join(project_root, 'ies_data.csv')
        
        # --- CORREÇÃO 2: MUDAR O DELIMITADOR PARA VÍRGULA ---
        df = pd.read_csv(csv_path, delimiter=',', encoding='latin1')
        
        total_rows = len(df)
        print(f"Total de {total_rows} registros a serem processados.")

        for index, row in df.iterrows():
            if (index + 1) % 100 == 0:
                print(f"Processando linha {index + 1}/{total_rows}...")

            # --- CORREÇÃO 3: USAR OS NOMES DE COLUNA CORRETOS ---
            nome_ies = row['NOME_DA_IES']
            sigla_ies = row['SIGLA']

            # Verifica se a instituição já existe para evitar duplicatas
            db_instituicao = db.query(Instituicao).filter_by(
                nome=nome_ies, 
                sigla=sigla_ies
            ).first()

            if not db_instituicao:
                nova_instituicao = Instituicao(
                    nome=nome_ies,
                    sigla=sigla_ies,
                    mantenedora_id=mantenedora_id_padrao # Usa o ID da mantenedora padrão
                )
                db.add(nova_instituicao)

        print("Finalizando a inserção dos dados...")
        db.commit()
        print("Carga de dados concluída com sucesso!")

    finally:
        db.close()

if __name__ == "__main__":
    load_data()