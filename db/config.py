from .connection_string import CONNECTION

config = {
    'sqlite': 'sqlite:////tmp/test.db',
    'mysql': 'mysql+pymysql://' + CONNECTION,
}