#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: list to be checked
 * Return: 0 if there are no cycles else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *list_check = list;

	while (!list)
		return (0);
	while (list_check->next && list_check->next->next)
	{
		list = list->next;
		list_check = list_check->next->next;
		if (list == list_check)
			return (1);
	}

	return (0);
}
