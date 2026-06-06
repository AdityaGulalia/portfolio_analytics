import logging

def setup_logger():
    logging.basicConfig(filename='/Users/adityagulalia/Desktop/py/track_it/reports/portfolio.log',
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
