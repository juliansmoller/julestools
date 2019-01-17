import pandas as pd
import xlsxwriter

class ExcelWorkbook:
    formats = [ 
        ('money', 14, {'num_format':'$#,##0.00'}),
        ('date', 10, {'num_format':'mm/dd/yy'}),
        ('percent', 10, {'num_format':'0.00%'}),
        ('text', 14, {'align':'left'}),
        ('int', 10, {'align':'right'}),
        ('bool', 10, {'align':'center'}),
        ('default', 10, {'align':'left'}),
        ('header', None, {'bold': True, 'align': 'center','bottom':1,'text_wrap':True})
    ]
    def __init__(self,path):
        self.path = path
        self.workbook = xlsxwriter.Workbook(path)
        self.sheets = {}
        self.widths = {f[0]:f[1] for f in self.formats if f[1] is not None}
        self.formats = {f[0]:self.workbook.add_format(f[2]) for f in self.formats if f[2] is not None}
    def fill_columns(self, data, sheet, col_types, header_row=0):
        '''Writes dataframe to Excel sheet using the formats specified in col_types;
        col_types is a dict that maps column names to text values, e.g. amt_invested: 'money', 
        which in turn can be used to look up the format and width'''
        for c,col in enumerate(data.columns):
            col_type = col_types.get(col,None)
            col_format = self.formats.get(col_type, self.formats['default'])
            col_width = self.widths.get(col_type, self.widths['default'])
            sheet.set_column(c,c,col_width)
            for i,value in enumerate(data[col]):
                r = header_row+i+1
                v = value if pd.notnull(value) else ''
                sheet.write(r,c,v,col_format)
        return
    def add_sheet(self,name,data,cols):
        # Recast columns as dataframe for easy lookup
        cols = pd.DataFrame(cols,columns=['old_name','new_name','data_type'])
        # Create worksheet
        self.sheets[name] = self.workbook.add_worksheet(name)
        # Filter data for important columns
        export = data[list(cols.old_name)].copy() 
        # Rename columns
        cols_to_rename = cols.set_index('old_name')['new_name'].to_dict()
        export = export.rename(index=str,columns=cols_to_rename) # Rename columns
        # Write header row (column names)
        header_row = 0
        self.sheets[name].set_row(header_row,45) # set height of header row
        for c,col in enumerate(export.columns): # write header row (column names)
            self.sheets[name].write(header_row,c,col,self.formats['header'])
        # Write data (column values)
        col_types = cols.set_index('new_name')['data_type'].to_dict()
        self.fill_columns(export, self.sheets[name], col_types)
        return
    def close(self):
        self.workbook.close()
        return