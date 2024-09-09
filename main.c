#include "simple.h"

int main() {
    char *command;
    init();
    while(1){
        printf(">");
        command = getInput();

        if(strlen(command) != 0){
            execute(command);
            free(command);
        }
    }
    return 0;
}