import datetime
import art as art

from aplication.salary import calculate_salary
from aplication.db.people import get_employees
from datetime import datetime

if __name__ == '__main__':
    print(datetime.today().strftime('%d/%m/%Y'))
    calculate_salary()
    get_employees()
    print(art.text2art('package', font='art'))




