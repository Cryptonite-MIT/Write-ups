Used strings command on the file and found this 

```
   1197 BKIAYQ^CH
   11a1 XONuELuRH
   11b4 EXYW
   2008 Oh no, you found this: %s
```

Opened the file on ghidra and found the function that used this string 

```c 
void zxc(void)

{
  size_t sVar1;
  char f [128];
  char x [20];
  int k;
  int i;
  
  builtin_strncpy(x,"BKIAYQ^CXONuELuREXYW",20);
  i = 0;
  while( true ) {
    sVar1 = strlen(x);
    if (sVar1 <= (ulong)(long)i) break;
    f[i] = x[i] ^ 42;
    i = i + 1;
  }
  sVar1 = strlen(x);
  f[sVar1] = '\0';
  printf("Oh no, you found this: %s\n",f);
  return;
}
```

Simple XOR operation so i used CodeChef to reverse it 

`hacks{tired_of_xors}`


