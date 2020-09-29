import sys
from tensorflow.python.compiler.tensorrt import trt_convert as trt

path = sys.argv[1]

converter = trt.TrtGraphConverterV2(input_saved_model_dir=path)
converter.convert()
converter.save(f'{path}_optimizadoTRT')
