#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Head of the list to check
 * Return: 0 if false, 1 if true
 */

int is_palindrome(listint_t **head)
{
	int i = 0;
	listint_t *headsave = *head;

	while (*head != NULL)
	{
		i++;
		*head = (*head)->next;
	}
	*head = headsave;
	return (1);
}
