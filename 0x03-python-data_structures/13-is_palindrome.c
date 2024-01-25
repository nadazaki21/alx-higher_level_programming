#include "lists.h"
#include <stdio.h>
// listint_t *reverse_list(listint_t *head, int node_number)
// {
//     if ((node_number%2) == 0)
//     {
//         for
//     }
    
// }
/**
 * is_palindrome - function to check if a linked list is palindrone or not
 * @head: the head of the linked list
*/
int is_palindrome(listint_t **head)
{
    int node_number = 0, i;
    listint_t *pointer = head, *temp;

    if ((*head)->next = NULL || (*head) == NULL)
        return (1);
    
    while(1)
    {
        node_number++;
        pointer = pointer->next;
        if (pointer->next == NULL)
            break;  
    }

    if ((node_number % 2) == 0)
    {
        pointer = *head;
        for (i = 1 ; i <= (node_number/2)+1 ; i++)
            pointer = pointer->next;
        
        temp = *head;
        *head = pointer;
        pointer = temp;
    }
    else
    {

    }
    
    
    

}