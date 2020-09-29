import tensorflow as tf


model = tf.keras.models.load_model('nuevoModeloBinario10epochs.h5')
model.save('frozen_graph.pb') #??

