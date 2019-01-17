import pandas as pd
import jdate
import datetime


def get_accrual_schedule(date_start, date_end, interest_rate, accrual_dates, advances, paydowns):
    schedule = _form_accrual_schedule(
        date_start, date_end, interest_rate, accrual_dates, advances, paydowns)
    schedule = _fill_accrual_schedule(schedule)
    return schedule

def _form_accrual_schedule(date_start, date_end, interest_rate, accrual_dates, advances, paydowns):
    schedule = pd.DataFrame(index=jdate.get_date_range(date_start, date_end))
    schedule['n360'] = [0]+[jdate.days360(d1,d2) for d1,d2 in zip(schedule.index[:-1],schedule.index[1:])]
    schedule['daily_rate'] = schedule['n360'].map(lambda n: (n/360)*interest_rate)
    schedule['is_accrual_date'] = schedule.index.map(lambda x: (x.month,x.day) in accrual_dates)
    schedule['amt_advanced'] = schedule.index.map(lambda x: float(advances.get(x,0)))
    schedule['amt_paydown'] = schedule.index.map(lambda x: float(paydowns.get(x,0)))
    return schedule

def _fill_accrual_schedule(schedule):
    principal = 0
    accrued = 0
    calculated = []
    for ix,d in schedule.reset_index().iterrows():
        d['principal_at_start'] = principal # value at end of prior day
        d['accrued_at_start'] = accrued # value at end prior day
        d['balance_at_start'] = principal+accrued
        # Accrue interest
        d['daily_accrual'] = d.daily_rate*d.principal_at_start
        accrued = d.accrued_at_start + d.daily_accrual
        # Apply accrued interest to principal (if accrual date)
        if d.is_accrual_date:
            principal += accrued
            accrued = 0
        # Adjust principal based on advances (e.g. on first day)
        principal += d.amt_advanced
        # Allocate paydown to principal and accrued
        d['paydown_accrued'] = min(d.amt_paydown, accrued) # first pay accrued interest
        d['paydown_principal'] = min(d.amt_paydown - d.paydown_accrued, principal) # then pay principal
        d['paydown_extra'] = d.amt_paydown - d.paydown_accrued - d.paydown_principal
        # Adjust principal and accrued based on paydown
        accrued -= d.paydown_accrued
        principal -= d.paydown_principal
        # Record end of day values
        d['principal_at_end'] = principal
        d['accrued_at_end'] = accrued
        d['balance_at_end'] = principal+accrued
        calculated.append(d)
    calculated = pd.DataFrame(calculated).set_index('index')
    return calculated

def test():
    return get_accrual_schedule(
        datetime.date(2018,2,20),
        datetime.date(2018,4,20),
        0.20,
        [(1,1),(3,1),(6,1),(9,1)],
        {datetime.date(2018,2,20):10000},
        {datetime.date(2018,2,25):500, datetime.date(2018,4,10):15000}
        )
