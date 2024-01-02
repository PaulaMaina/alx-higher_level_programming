#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: points to head node
 * @number: number to be inserted
 *
 * Return: address of the new node or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *curr_node;

	if (!head)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	curr_node = *head;
	if (*head == NULL)
		*head = new_node;
	else if (number < curr_node->n)
	{
		new_node->next = curr_node;
		*head = new_node;
	}
	else
	{
		while (curr_node->next)
		{
			if (number > curr_node->next->n)
				curr_node = curr_node->next;
			else
				break;
		}
		new_node->next = curr_node->next;
		curr_node->next = new_node;
	}

	return (new_node);
}
