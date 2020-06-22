#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
/**
 * infinite_while - infinite while loop.
 * Return: 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - Fvoid main
 * Return: 0
 */
int main(void)
{
	pid_t pid;
	size_t s = 0;

	while (s > 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			s++;
		}
		else
			exit(0);
	}
	infinite_while();

	return (0);
}
