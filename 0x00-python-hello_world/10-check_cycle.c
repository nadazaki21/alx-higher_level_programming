#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks is linked list is cylic
 * @list: the linked list to check
 * Return: 0 or 1 to indicate if the linked list is cylic or not
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1, *ptr2;

	if (list == NULL || list->next == NULL)
		return (0);

	ptr1 = list->next->next; /* moves 2 stepps*/
	ptr2 = list->next;		 /* moves 1 step s*/

	while (ptr1 && ptr2 && ptr1->next)
	{
		if (ptr1 == ptr2)
			return (1);
		ptr1 = ptr1->next->next;
		ptr2 = ptr2->next;
	}
}
