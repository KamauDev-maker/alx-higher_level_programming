#include "lists.h"
#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
/**
 * is_palindrome - check if linked list is a palindrome
 * @head: pointer to pointer head
 * Return: o if is not a palindrome, 1 if is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check_pali(head, *head));
}
/**
 *check_pali - function to if the list is palindrome
 *@head: pointer to the start
 *@tail: pointer to the end
 *Return: 0 if not palindrome else 1
 */
int check_pali(listint_t **head, listint_t *tail)
{
	if (tail == NULL)
		return (1);
	if (check_pali(head, tail->next) && (*head)->n == tail->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

