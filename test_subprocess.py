import multiprocessing as mp
import sys

def test_in_subprocess():
    import sys
    sys.stdout.write('Subprocess started\n')
    sys.stdout.flush()
    
    # Import everything livekit-agents imports
    sys.stdout.write('Importing torch...\n')
    sys.stdout.flush()
    import torch
    sys.stdout.write(f'Torch OK: {torch.__version__}, CUDA: {torch.cuda.is_available()}\n')
    sys.stdout.flush()
    
    sys.stdout.write('Importing livekit.agents...\n')
    sys.stdout.flush()
    import livekit.agents
    sys.stdout.write('livekit.agents OK\n')
    sys.stdout.flush()
    
    sys.stdout.write('Importing silero...\n')
    sys.stdout.flush()
    from livekit.plugins import silero
    sys.stdout.write('silero OK\n')
    sys.stdout.flush()
    
    sys.stdout.write('Importing turn_detector...\n')
    sys.stdout.flush()
    from livekit.plugins.turn_detector.multilingual import _EUORunnerMultilingual
    sys.stdout.write('Imported runner\n')
    sys.stdout.flush()
    
    runner = _EUORunnerMultilingual()
    sys.stdout.write('Created runner\n')
    sys.stdout.flush()
    
    runner.initialize()
    sys.stdout.write('Runner initialized OK!\n')
    sys.stdout.flush()

if __name__ == '__main__':
    mp.set_start_method('spawn', force=True)
    p = mp.Process(target=test_in_subprocess)
    p.start()
    p.join(timeout=120)
    print(f'Exit code: {p.exitcode}')

