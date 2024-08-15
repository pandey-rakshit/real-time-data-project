import multiprocessing
from src import imputer, retriever

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=imputer.simulate_and_insert_data)
    p2 = multiprocessing.Process(target=retriever.fetch_and_process_data)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
