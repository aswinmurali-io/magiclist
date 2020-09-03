#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct magic_node
{
    char *data;
    struct magic_node *next;
};

typedef struct magic_node *magic_list;

struct magic_node inline *create_magic_list()
{
    struct magic_node *head = (struct magic_node *)malloc(sizeof(struct magic_node));
    head->data = NULL;
    head->next = NULL;
    return head;
}

void append(struct magic_node *head, const char *content)
{
    struct magic_node *newnode = (struct magic_node *)malloc(sizeof(struct magic_node));
    newnode->data = (char *)malloc(sizeof(content));
    newnode->next = NULL;
    head->next = newnode;
    strcpy(newnode->data, content);
}

void traverse(struct magic_node *head)
{
    struct magic_node *copy = head;
    if(head == NULL)
        printf("[MAGIC LIST WARNING]: The magic list is not init! assign with list with create_magic_list()'s return type");
    if(head->next == NULL)
        return;
    copy = copy->next; // To not traverse the head which has NULL as data
    while (copy != NULL)
    {
        printf("%s", copy->data);
        copy = copy->next;
    }
}

int main()
{
    magic_list test = create_magic_list();
    append(test, "Hi");
    append(test, "Hi2");
    traverse(test);
    return 0;
}
