#include "hash_tables.h"
/**
 * hash_table_create - returns pointer to newly created hash function
 * @size: the size of the needed hash table
 * Return: a pointer to tthe newly created hash table
*/
hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *ht = malloc(sizeof(hash_table_t));

	if (ht == NULL)
		return (NULL);

	ht->array = malloc(sizeof(hash_node_t *) * size);
	if (ht->array == NULL)
		return (NULL);

	return (ht);

}
