import io
import sys
from sqlalchemy import create_engine, MetaData
from sqlacodegen.codegen import CodeGenerator

def generate_model( outfile = None):
    engine = create_engine(f'mysql+mysqlconnector://testdbuser:MySq1DB2k22@corp.rigelsoft.com/test_db')
    metadata = MetaData(bind=engine)
    metadata.reflect()
    outfile = io.open(outfile, 'w', encoding='utf-8') if outfile else sys.stdout
    generator = CodeGenerator(metadata)
    generator.render(outfile)

if __name__ == '__main__':
    generate_model( 'db.py')