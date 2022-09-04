import pandas as pd
def get_today_plan(day_number):
    with open("schedule.csv", "r", encoding="utf-8", errors="ignore") as pfile:
        plan = pd.read_csv(pfile)
        plan_list = plan.values
    plan_today = plan_list.tolist()[day_number]
    return plan_today


def sort_today_plan(date):
    last_element = ''
    same_element_count = 1
    plan_today_sorted = []
    for i in get_today_plan(date):
        if i == last_element:
            same_element_count += 1
            plan_today_sorted.pop()
            plan_today_sorted.append(f"{i} x{same_element_count}")
            last_element = i
        else:
            same_element_count = 1
            plan_today_sorted.append(i)
            last_element = i
    return plan_today_sorted