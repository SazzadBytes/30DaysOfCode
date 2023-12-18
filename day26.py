def check_date():
    return_date=input().split()
    due_date=input().split()
    return return_date,due_date

def calculate_fine(return_date,due_date):
    return_day,return_month,return_year=map(int,return_date)
    due_day,due_month,due_year=map(int,due_date)
    if return_year>due_year:
        print("10000")
    elif return_year==due_year and return_month>due_month:
        total_month=return_month-due_month
        total_fine=total_month*500
        print(total_fine)
    elif return_year==due_year and return_month==due_month and return_day>due_day:
        total_day=return_day-due_day
        total_fine=total_day*15
        print(total_fine)
    else:
        print("0")
if __name__=='__main__':
    return_date,due_date=check_date()
    calculate_fine(return_date,due_date)