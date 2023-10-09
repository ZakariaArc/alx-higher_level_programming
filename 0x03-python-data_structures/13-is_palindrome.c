#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
/**
 * reverse_list - reverse a linked list
 * @head: a pointer to the head of the list
 * Return: a pointer to the new head of the reversed list
 */

listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: a pointer to the head of the list
 * Return: 1 if it's a palindrome, otherwise 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *second_half;
	listint_t *prev_slow = *head;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		prev_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}
	second_half = reverse_list(slow);
	slow = *head;
	while (second_half != NULL)
	{
		if (second_half->n != slow->n)
		{
			is_palindrome = 0;
			break;
		}
		second_half = second_half->next;
		slow = slow->next;
	}
	reverse_list(second_half);
	prev_slow->next = second_half;
	return (is_palindrome);
}
