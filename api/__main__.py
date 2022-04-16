if __name__ == '__main__':
    
    import os

    try: 
        os.system('cd api && python -m flask run --host=0.0.0.0')
    except KeyboardInterrupt:
        print('Exit.')