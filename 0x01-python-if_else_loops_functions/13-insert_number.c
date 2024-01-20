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
        if ((cursor->n < number) && (cursor->next != NULL))
        {
            if (cursor->next->n > number)
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
        }
        else if (((*head)->n > number))
        {
            new_node = malloc(sizeof(listint_t));
            if (new_node == NULL)
                return (NULL);

            new_node->n = number;
            new_node->next = *head;
            *head = new_node;
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
        else if (cursor->n == number)
        {
            prev_node = cursor;
            next_node = cursor->next;

            new_node = malloc(sizeof(listint_t));
            if (new_node == NULL)
                return (NULL);

            new_node->n = number;
            prev_node->next = new_node;

            if (cursor->next == NULL)
                new_node->next = NULL;
            else
                new_node->next = next_node;
            
            break;   
        }
        cursor = cursor->next;
    }
    return (new_node);
}