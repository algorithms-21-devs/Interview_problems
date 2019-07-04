import double_linked_list as dll




ll_sample = dll.DoubleLinkedList()
'''
#Test Exception
ll_sample.delete_start()
ll_sample.delete_end()
ll_sample.traverse()
'''

#Test insert
ll_sample.insert_end('h')
ll_sample.insert_start('e')
ll_sample.insert_start('l')
ll_sample.insert_start('l')
ll_sample.insert_start('o')
ll_sample.traverse()
print('\n')
ll_sample.delete_end()
ll_sample.delete_end()
ll_sample.traverse()

print('\n')
ll_sample.delete_start()
ll_sample.delete_start()
ll_sample.traverse()

#Testing Exceptions - works
#ll_sample.insert_end(None)
#ll_sample.insert_start(None)
