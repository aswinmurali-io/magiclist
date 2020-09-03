#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAGIC_MEMORY_BLOCK (struct magic_node *)malloc(sizeof(struct magic_node))

struct magic_node
{
    char *data;
    struct magic_node *next;
};

typedef struct magic_node *magic_list;
typedef struct magic_node *magic_head;

struct magic_node *create_magic_list()
{
    struct magic_node *head = MAGIC_MEMORY_BLOCK;
    head->data = NULL;
    head->next = NULL;
    return head;
}

void append(struct magic_node *head, const char *content)
{
    struct magic_node *newnode = MAGIC_MEMORY_BLOCK;
    struct magic_node *temp = head;

    while (temp->next != NULL)
        temp = temp->next;
    temp->next = newnode;

    newnode->next = NULL;

    // make string memory block and then strcpy
    newnode->data = (char *)malloc(sizeof(content));
    strcpy(newnode->data, content);
}

void traverse(struct magic_node *head)
{
    struct magic_node *temp = head;
    if (head == NULL)
        printf("[MAGIC LIST WARNING]: The magic list is not init! assign with list with create_magic_list()'s return type");
    if (head->next == NULL)
        return;
    temp = temp->next; // To not traverse the head which has NULL as data
    while (temp != NULL)
    {
        printf("%s\n", temp->data);
        temp = temp->next;
    }
}

int main()
{
    magic_list test = create_magic_list();
    magic_head head = test;
    append(test, "Hi");
    append(test, "Hi2");
    append(test, "Hi3");
    traverse(test);
    return 0;
}
