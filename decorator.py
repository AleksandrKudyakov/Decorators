from datetime import datetime
import requests

decorator_logs = 'decorator_logs.txt'
def log_decorator(path):
    def _log_decorator(oldfunction):
        def foo(*args, **kwargs):
            date_time = datetime.now()
            str_time = date_time.strftime('%Y-%m-%d время %H-%M-%S')
            func_name = oldfunction.__name__
            result = oldfunction(*args, **kwargs)
            with open(path,'a', encoding='utf-8') as file:
                file.write(f'\nДата вызова функции: {str_time}\n'
                           f'Имя функции: {func_name}\n'
                           f'Аргументы функции: {args, kwargs}\n'
                           f'Возвращаемое значение функции: {result}\n'
                           f'{"*"*50}\n')
            return result
        return foo
    return _log_decorator
    
@log_decorator(decorator_logs)
def get_status(*args):
    url = ','.join(args)
    response = requests.get(url=url)
    return response.status_code

@log_decorator(decorator_logs)
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

if __name__ == '__main__':
    get_status('https://habr.com/ru/all/')
    factorial(8)