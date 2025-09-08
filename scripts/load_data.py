import sys
import os
import pandas as pd

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from sqlalchemy.orm import Session
from api.core.database import SessionLocal, engine
from api.models.base import Mantenedora, Instituicao, Base

def load_data():
    Base.metadata.create_all(bind=engine)
    
    db: Session = SessionLocal()

    try:
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
        df = pd.read_csv(csv_path, delimiter=',', encoding='latin1')
        
        total_rows = len(df)
        print(f"Total de {total_rows} registros a serem processados.")

        for index, row in df.iterrows():
            if (index + 1) % 100 == 0:
                print(f"Processando linha {index + 1}/{total_rows}...")

            nome_ies = row['NOME_DA_IES']
            sigla_ies = row['SIGLA']
            
            # <<< INÍCIO DA MODIFICAÇÃO >>>
            municipio_ies = row['MUNICIPIO']
            uf_ies = row['UF']
            # <<< FIM DA MODIFICAÇÃO >>>

            db_instituicao = db.query(Instituicao).filter_by(
                nome=nome_ies, 
                sigla=sigla_ies
            ).first()

            if not db_instituicao:
                nova_instituicao = Instituicao(
                    nome=nome_ies,
                    sigla=sigla_ies,
                    # <<< INÍCIO DA MODIFICAÇÃO >>>
                    municipio=municipio_ies,
                    uf=uf_ies,
                    # <<< FIM DA MODIFICAÇÃO >>>
                    mantenedora_id=mantenedora_id_padrao
                )
                db.add(nova_instituicao)

        print("Finalizando a inserção dos dados...")
        db.commit()
        print("Carga de dados concluída com sucesso!")

    finally:
        db.close()

if __name__ == "__main__":
    load_data()