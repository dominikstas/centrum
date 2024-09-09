#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <dirent.h>
#include <sys/stat.h>
#include <fcntl.h>

void execute(char *command);
void echo(char *text);
void exitS();
void help();
void init();
char* getInput();
void copyFile(const char *source, const char *destination);
void moveFile(const char *source, const char *destination);
void catFile(const char *file);

void execute(char *command) {
    if (strncmp(command, "echo ", 5) == 0) {
        char *text = command + 5; 
        if (strlen(text) > 0) {
            echo(text);
        } else {
            printf("Usage: echo [text]\n");
        }
    } else if (strcmp(command, "exit") == 0) {
        exitS();
    } else if (strcmp(command, "help") == 0) {
        help();
    } else if (strncmp(command, "cd ", 3) == 0) {
        char *dir = command + 3;
        if(chdir(dir) != 0) {
            perror("cd");
        }
    } else if (strcmp(command, "ls") == 0) {
        DIR *d;
        struct dirent *dir;
        d = opendir(".");
        if (d) {
            while ((dir = readdir(d)) != NULL) {
                printf("%s\n", dir->d_name);
            }
            closedir(d);
        }
    } else if (strncmp(command, "mkdir ", 6) == 0) {
        char *dir = command + 6;
        if(mkdir(dir, 0777) != 0) {
            perror("mkdir");
        }
    } else if (strcmp(command, "pwd") == 0) {
        char cwd[1024];
        if (getcwd(cwd, sizeof(cwd)) != NULL) {
            printf("%s\n", cwd);
        } else {
            perror("pwd");
        }
    } else if (strncmp(command, "rm ", 3) == 0) {
        char *file = command + 3;
        if(remove(file) != 0) {
            perror("rm");
        }
    } else if (strncmp(command, "touch ", 6) == 0) {
        char *file = command + 6;
        FILE *fp = fopen(file, "w");
        if (fp == NULL) {
            perror("touch");
        } else {
            fclose(fp);
        }
    } else if (strncmp(command, "cp ", 3) == 0) {
        char *args = command + 3;
        char *source = strtok(args, " ");
        char *destination = strtok(NULL, " ");
        if (source && destination) {
            copyFile(source, destination);
        } else {
            printf("Usage: cp [source] [destination]\n");
        }
    } else if (strncmp(command, "mv ", 3) == 0) {
        char *args = command + 3;
        char *source = strtok(args, " ");
        char *destination = strtok(NULL, " ");
        if (source && destination) {
            moveFile(source, destination);
        } else {
            printf("Usage: mv [source] [destination]\n");
        }
    } else if (strncmp(command, "cat ", 4) == 0) {
        char *file = command + 4;
        if (strlen(file) > 0) {
            catFile(file);
        } else {
            printf("Usage: cat [file]\n");
        }
    } else {
        printf("Unknown command: %s\n", command);
    }
}

void echo(char *text) {
    printf("%s\n", text);
}

void exitS() {
    printf("Thanks for using\n");
    exit(0);
}

void help() {
    printf("--------------------------------------\n");
    printf("All commands:\n");
    printf("help - show all commands\n");
    printf("echo [text] - write a text\n");
    printf("cd [directory] - change directory\n");
    printf("ls - list directory contents\n");
    printf("mkdir [directory] - create a directory\n");
    printf("pwd - print working directory\n");
    printf("rm [file] - remove a file\n");
    printf("touch [file] - create an empty file\n");
    printf("cp [source] [destination] - copy a file\n");
    printf("mv [source] [destination] - move/rename a file\n");
    printf("cat [file] - display file contents\n");
    printf("exit - exit the terminal\n");
    printf("--------------------------------------\n");
}

void init() {
    system("clear");
    printf("Welcome!\n");
}

char* getInput() {
    char *input = NULL;
    size_t bufferSize = 0;

    getline(&input, &bufferSize, stdin);
    input[strcspn(input, "\n")] = '\0';

    return input;
}

void copyFile(const char *source, const char *destination) {
    int src_fd = open(source, O_RDONLY);
    if (src_fd < 0) {
        perror("cp");
        return;
    }

    int dest_fd = open(destination, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (dest_fd < 0) {
        perror("cp");
        close(src_fd);
        return;
    }

    char buffer[4096];
    ssize_t bytesRead, bytesWritten;

    while ((bytesRead = read(src_fd, buffer, sizeof(buffer))) > 0) {
        bytesWritten = write(dest_fd, buffer, bytesRead);
        if (bytesWritten != bytesRead) {
            perror("cp");
            close(src_fd);
            close(dest_fd);
            return;
        }
    }

    if (bytesRead < 0) {
        perror("cp");
    }

    close(src_fd);
    close(dest_fd);
}

void moveFile(const char *source, const char *destination) {
    if (rename(source, destination) != 0) {
        perror("mv");
    }
}

void catFile(const char *file) {
    FILE *fp = fopen(file, "r");
    if (fp == NULL) {
        perror("cat");
        return;
    }

    char buffer[4096];
    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        printf("%s", buffer);
    }

    fclose(fp);
}
