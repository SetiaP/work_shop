import os, platform, logging

if platform.platform().startswith('Windows'):
    berkas_logging = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
else:
    berkas_logging = os.path.join(os.getenv('HOME'), 'test.log')

print("Logging ke", berkas_logging)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename = berkas_logging,
    filemode = 'w',
)

logging.debug("Memulai program")
logging.info("Mengerjakan sesuatu")
logging.warning("Matikan sekarang")