#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - function that inserts number into a sorted singly linked list
 * @head: the pointer to a pointer pointing to the first node of the list
 * @number: the value to be inserted
 * Return: address of the new node, if it failed return NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	current = *head;
	while (current->next != NULL && current->next->n < number)
		current = current->next;
	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}
