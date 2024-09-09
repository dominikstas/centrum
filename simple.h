#ifndef SIMPLE_H
#define SIMPLE_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>

void execute(char *command);
void echo(char *text);
void exitS();
void help();
void init();
char* getInput();
void copyFile(const char *source, const char *destination);
void moveFile(const char *source, const char *destination);
void catFile(const char *file);


#endif
