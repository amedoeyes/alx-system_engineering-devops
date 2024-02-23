#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - runs forever
 *
 * Return: 0 (lie)
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
 * main - creates 5 zombie processes
 *
 * Return: 0
 */

int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
			break;
		printf("Zombie process created, PID: %d\n", pid);
	}

	if (pid != 0)
		infinite_while();

	return (0);
}
