import multiprocessing as mp
import sys

def test_in_subprocess():
    import sys
    sys.stdout.write('Subprocess started\n')
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
    p.join(timeout=60)
    print(f'Exit code: {p.exitcode}')

