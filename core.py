import hashlib as hasher
import datetime as date

class Block:
    '''
    This is a Block in block chain
    consists all the information about every activity
    '''

    def __init__(self, index, timestamp, information, previous_hash):
      self.index = index
      self.timestamp = timestamp
      self.data = information
      self.previous_hash = previous_hash
      self.hash = self.blocks_hash()
  
    def blocks_hash(self):
      sha = hasher.sha256()
      sha.update(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash))
      return sha.hexdigest()

# Generate blocks and append in ledger
class Blockchain:
    '''
    This is a blockchain it creates a genesis block
    and gives the capability to create next block
    '''
    def __init__(self):
        '''
        Basically generates genesis block and assign it to 'blockchain'
        '''
        some = Block(0,date.datetime.now(),'This is genesis block of sikka',"0")
        self.blockchain = [some]

    # Generate all later blocks in the blockchain
    def next_block(self,last_block):
        '''
        create next block using previous block hash
        '''
        this_index = last_block.index + 1
        this_timestamp = date.datetime.now()
        this_data = "Hey! I'm block in sikka coin" + str(this_index)
        this_hash = last_block.hash
        return Block(this_index, this_timestamp, this_data, this_hash)

