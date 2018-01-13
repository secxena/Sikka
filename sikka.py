from core import Block,Blockchain

# Create the blockchain 
BC = Blockchain()
blockchain = BC.blockchain
previous_block = blockchain[0]
#will generate blockchain of 100 blocks
num_of_blocks_to_add = 100

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
  block_to_add = BC.next_block(previous_block)
  blockchain.append(block_to_add)
  previous_block = block_to_add
  print "Block #{} has been added to the sikka blockchain!".format(block_to_add.index)
  print "Hash: {}\n".format(block_to_add.hash) 
