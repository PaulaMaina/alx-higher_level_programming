#include "lists.h"

/**
 * is_palindrome - checks is a singly linked list is a palindrome
 * @head: head node
 *
 * Return: 1 if it's a palindrome else 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int len = 0, a = 0;
	int x[10000];

	temp = *head;
	if ((*head) == NULL)
		return (1);
	while (temp != NULL)
	{
		len++;
		temp = temp->next;
	}
	if (len == 1)
		return (1);
	temp = *head;
	while (temp != NULL)
	{
		x[a] = temp->n;
		temp = temp->next;
		a++;
	}
	for (a = 0; a <= len / 2; a++)
	{
		if (x[a] != x[len - a - 1])
			return (0);
	}
	return (1);
}
