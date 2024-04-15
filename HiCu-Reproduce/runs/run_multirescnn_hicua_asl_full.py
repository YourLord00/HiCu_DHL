# import os

# # Edit value of num_runs to change the number of repeat runs
# num_runs = 1
# for i in range(1, num_runs + 1):
#     print(f"Starting run No. {i} of {num_runs}")
    
#     cmd = (
#         "python main.py "
#         "--model MultiResCNN "
#         "--vocab ./data/mimic3/vocab.csv "
#         "--decoder HierarchicalHyperbolic "
#         "--loss ASL "
#         "--asl_config 1,0,0.05 "
#         "--Y full "
#         "--data_path ./data/mimic3/train_full.csv "
#         "--MAX_LENGTH 4096 "
#         "--embed_file ./data/mimic3/processed_full_100.embed "
#         "--tune_wordemb "
#         "--batch_size 8 "
#         "--lr 5e-5 "
#         "--n_epochs 2,3,5,10,50 "
#         "--criterion prec_at_8 "
#         "--random_seed 0 "
#         "--num_workers 1 "
#     )

#     os.system(cmd)

# print(f"Completed all {num_runs} runs")



import os
import multiprocessing as mp

# Edit value of num_runs to change the number of repeat runs
num_runs = 1

def run_command(cmd):
    os.system(cmd)

if __name__ == '__main__':
    # Create a new multiprocessing context with 'spawn' start method
    mp_context = mp.get_context('spawn')

    for i in range(1, num_runs + 1):
        print(f"Starting run No. {i} of {num_runs}")
        cmd = (
            "python main.py "
            "--model MultiResCNN "
            "--vocab ./data/mimic3/vocab.csv "
            "--decoder HierarchicalHyperbolic "
            "--loss ASL "
            "--asl_config 1,0,0.05 "
            "--Y full "
            "--data_path ./data/mimic3/train_full.csv "
            "--MAX_LENGTH 4096 "
            "--embed_file ./data/mimic3/processed_full_100.embed "
            "--tune_wordemb "
            "--batch_size 8 "
            "--lr 5e-5 "
            "--n_epochs 2,3,5,10,50 "
            "--criterion prec_at_8 "
            "--random_seed 0 "
            "--num_workers 1 "
        )
        process = mp_context.Process(target=run_command, args=(cmd,))
        process.start()
        process.join()

    print(f"Completed all {num_runs} runs")