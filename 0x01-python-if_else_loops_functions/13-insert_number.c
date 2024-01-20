#include "lists.h"
/**
 * 
*/
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *cursor = *head, *new_node, *prev_node, *next_node; 
    
    if (cursor == NULL)
    {
        new_node = malloc(sizeof(listint_t));
            if (new_node == NULL)
                return (NULL);
            
            new_node->n = number;
            new_node->next = NULL;
            *head = new_node;
            return (new_node);
    }
    
    while (cursor != NULL)
    {   /*  insert in the middle  */
        if ((cursor->n < number) && (cursor->next->n > number))
        {
            prev_node = cursor;
            next_node = cursor->next;
            new_node = malloc(sizeof(listint_t));
            if (new_node == NULL)
                return (NULL);
            new_node->n = number;
            new_node->next = next_node;
            prev_node->next = new_node;
            break;
        }
        else if ((cursor->n > number) && ((cursor->next == NULL) || (cursor->next != NULL)))
        {
            /* if is it the whole list is biger than then number */
            new_node = malloc(sizeof(listint_t));
            if (new_node == NULL)
                return (NULL);

            new_node->n = number;
            new_node->next = cursor;
            break;
        }
        else if ((cursor->n < number) && (cursor->next == NULL))
        {
            prev_node = cursor;

            new_node = malloc(sizeof(listint_t));
            if (new_node == NULL)
                return (NULL);

            new_node->n = number;
            new_node->next = NULL;
            prev_node->next = new_node;
            
            break;
        }
        
        cursor = cursor->next;
    }
    return (new_node);
}