#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 *insert_node - inserts a number into a sorted singly linked list
 *@head: head pointer
 *@number: number to add
 *Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *temp;
	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	if (*head == NULL)
	{
		newnode->n = number;
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	else if (number <= (*head)->n)
	{
		newnode->n = number;
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	else
	{
		temp = *head;
		while (temp->next !=NULL && number > temp->next->n)
		{
			temp = temp->next;
		}
		newnode->n = number;
		newnode->next = temp->next;
		temp->next = newnode;
		return (newnode);
	}
	return (NULL);
}
