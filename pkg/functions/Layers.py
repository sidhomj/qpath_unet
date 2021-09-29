import tensorflow as tf

def conv_block(input, filters=64, kernel_size=(2,2),activation = tf.nn.relu, pool_size=(2,2), dropout =0.3):
    output = tf.keras.layers.Conv2D(filters=filters,kernel_size=kernel_size,activation=activation)(input)
    output = tf.keras.layers.Conv2D(filters=filters,kernel_size=kernel_size,activation=activation)(output)
    skip = output
    output = tf.keras.layers.MaxPool2D(pool_size=pool_size)(output)
    output = tf.keras.layers.Dropout(rate=dropout)(output)
    return skip,output

def deconv_block(input, conv_output, filters=64, kernel_size=(2,2), strides=3, dropout=0.3,activation=tf.nn.relu):
  output = tf.keras.layers.Conv2DTranspose(filters, kernel_size, strides = strides, padding = 'same')(input)
  output = tf.keras.layers.concatenate([output, conv_output])
  output = tf.keras.layers.Conv2D(filters=filters,kernel_size=kernel_size,activation=activation)(output)
  output = tf.keras.layers.Conv2D(filters=filters,kernel_size=kernel_size,activation=activation)(output)
  output = tf.keras.layers.Dropout(dropout)(output)
  return output

def encoder(input_dim=[256,256],input_channels=3):
    input_dim.append(input_channels)
    input = tf.keras.layers.Input(input_dim, dtype=tf.float32)
    s1,l1 = conv_block(input,filters=64)
    s2,l2 = conv_block(l1,filters=128)
    s3,l3 = conv_block(l2,filters=256)
    s4,l4 = conv_block(l3,filters=512)
    return tf.keras.Model(inputs=[input],outputs=[l4,s4,s3,s2,s1])

def bottleneck(input_dim,filters=1024):
    input = tf.keras.layers.Input(input_dim, dtype=tf.float32)
    s,l = conv_block(input,filters=filters)
    return tf.keras.Model(inputs=[input],outputs=[s])

def decoder(input_dim,conv_dims,output_dim,output_channels):
    input = tf.keras.layers.Input(input_dim, dtype=tf.float32)
    conv_outputs = []
    for _ in conv_dims:
        conv_outputs.append(tf.keras.layers.Input(_,dtype=tf.float32))

    d1 = deconv_block(input,conv_outputs[0])




# def decoder(input_dim,output_dim,output_channels):
#     input = tf.keras.layers.Input(input_dim, dtype=tf.float32)
#     deconv_block(input,)
#   l1, l2, l3, l4 = convs
#   deconv_block()
#
#   c6 = decoder_block(inputs, f4, n_filters=512, kernel_size=(3,3), strides=(2,2), dropout=0.3)
#   c7 = decoder_block(c6, f3, n_filters=256, kernel_size=(3,3), strides=(2,2), dropout=0.3)
#   c8 = decoder_block(c7, f2, n_filters=128, kernel_size=(3,3), strides=(2,2), dropout=0.3)
#   c9 = decoder_block(c8, f1, n_filters=64, kernel_size=(3,3), strides=(2,2), dropout=0.3)
#
#   outputs = tf.keras.layers.Conv2D(output_channels, (1, 1), activation='softmax')(c9)
#
#   return outputs


