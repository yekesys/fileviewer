
import src.filev_utils as fiu

CHUNK_SIZE = 16

fiu.view_file("src/filev_utils.py", base="hex", chunk_size=CHUNK_SIZE)
fiu.view_file("src/filev_utils.py", base="dec", chunk_size=CHUNK_SIZE)


