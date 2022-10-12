import pandas as pd

class ColumnNameDoesNotExists(Exception):
    """Raised if user try to access to a not existing column in Hmilerender.Renderer.Renderer
    """
    def __init__(self, column_name) -> None:
        super().__init__(self)
        self.column_name = column_name
    
    def __str__(self) -> str:
        return """%s is not an existing data column""" % (self.column_name)
    

class DataframeFormatException(Exception):
    """Raise an exception if the dataframe does not correspond to the Hmile specification.
    """
    def __init__(self, msg : str, dataframe : pd.DataFrame) -> None:
        super().__init__(self)
        self.msg = msg
        self.dataframe = dataframe
    
    def __str__(self) -> str:
        return f'{self.msg} : {self.dataframe.head()}'

class DataProviderArgumentException(Exception):
    """Raise an exception if the data provider argument is not valid.
    """
    def __init__(self, msg : str) -> None:
        super().__init__(self)
        self.msg = msg
    
    def __str__(self) -> str:
        return f'{self.msg}'