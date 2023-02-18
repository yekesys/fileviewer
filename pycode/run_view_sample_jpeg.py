
import src.filev_utils as fiu

CHUNK_SIZE = 16

fiu.view_file("data/sample.jpeg", base="hex", chunk_size=CHUNK_SIZE)
fiu.view_file("data/sample.jpeg", base="dec", chunk_size=CHUNK_SIZE)


