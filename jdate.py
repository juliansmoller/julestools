import datetime

def today():
    return datetime.date.today()
def today_str():
    return datetime.date.today().strftime('%Y_%m_%d')
def date_to_str(date):
    return date.strftime('%Y_%m_%d')
def date_to_month_id(date):
    return date.year*12 + date.month-1
def date_to_ym(date):
    return (date.year, date.month)
def date_to_qtr_id(date):
    return date.year*4 + (date.month-1)//3
def month_id_to_ym(x):
    return (x//12, x%12+1)
def ym_to_str(ym):
    return str(ym[0])+'_'+str(ym[1]).zfill(2)
def ym_to_qtr_id(ym):
    return ym[0]*4 + (ym[1]-1)//3
def qtr_id_to_yq(x):
    return (x//4,x%4+1)
def yq_to_str(yq):
    return str(yq[0])+'_Q'+str(yq[1])
def yq_to_qtr_id(yq):
    return yq[0]*4 + (yq[1]-1)
def yq_to_date(yq):
    return datetime.date(yq[0], yq[1]*3-2, 1) # first day of quarter
def date_to_yq(date):
    return qtr_id_to_yq(date_to_qtr_id(date))
def date_to_yq_str(date):
    return yq_to_str(date_to_yq(date))
def date_to_ym_str(date):
    return ym_to_str(date_to_ym(date))
def get_p_quarter_elapsed():
    '''Given todays date, determine the percent of the current quarter that has elapsed'''
    yq = date_to_yq(today()) # (year, month) for current quarter
    d0 = yq_to_date(yq) # first day of quarter 
    days_elapsed = (today()-d0).days
    days_in_quarter = 365/4 # about 91
    return days_elapsed/days_in_quarter
def get_projection_multiplier_for_quarter():
    yq_str = date_to_yq_str(today())
    p_elapsed = get_p_quarter_elapsed()
    multiplier = 1/p_elapsed
    return multiplier
def get_date_range(date0, date1):
    return [date0 + datetime.timedelta(n) for n in range(int((date1 - date0).days))]
def is_in_or_before_month(date,year,month):
    return date.year<year or (date.year==year and date.month<=month)
def get_month_range(dates):
    '''Return a list of (year,month) tuples spanning the first date to the last'''
    year_months = []
    dmin = dates.min()
    dmax = dates.max()
    xmin = dmin.year*12 + dmin.month - 1
    xmax = dmax.year*12 + dmax.month
    for x in range(xmin,xmax):
        year_months.append((x//12,x%12+1))
    return year_months
def get_month_id_from_date(date): 
    return date.year*12 + date.month-1
def get_month_id_from_year_month(ym):
    return ym[0]*12 + ym[1]-1
def get_year_month_from_month_id(x):
    return (x//12, x%12+1)
def get_quarter_id_from_date(date):
    return date.year*4 + (date.month-1)//3
def get_quarter_id_from_year_month(ym):
    return ym[0]*4 + (ym[1]-1)//3
def get_year_quarter_from_quarter_id(x):
    return (x//4,x%4+1)
def get_year_month_str(ym):
    return str(ym[0])+'_'+str(ym[1]).zfill(2)
def days360(date0,date1):
    '''Calculate the number of days between 2 dates based on Excel 30/360 function'''
    y0,m0,d0 = (date0.year,date0.month,date0.day)
    y1,m1,d1 = (date1.year,date1.month,date1.day)
    d0 = min(d0,30) # replace 31 with 30
    d1 = min(d1,30) # replace 31 with 30
    n_days = (y1-y0)*360 + (m1-m0)*30 + (d1-d0)
    return n_days