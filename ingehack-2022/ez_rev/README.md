# ez_rev

- First, we open the binary in ghidra.
- We look for the main function.

```C
undefined8 main(void)
{
  undefined8 uVar1;
  long in_FS_OFFSET;
  int local_1c0;
  undefined4 local_1b8 [40];
  undefined4 local_118 [40];
  byte local_78 [104];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  fwrite("Let me check your secret: ",1,0x1a,stdout);
  fgets((char *)local_78,100,stdin);
  fputc(10,stdout);
  local_1b8[0] = 0x12;
  local_1b8[1] = 0x3a;
  local_1b8[2] = 0x32;
  local_1b8[3] = 0x39;
  local_1b8[4] = 0x11;
  local_1b8[5] = 0xb;
  local_1b8[6] = 0x16;
  local_1b8[7] = 0x1d;
  local_1b8[8] = 0x1c;
  local_1b8[9] = 0x19;
  local_1b8[10] = 0x2d;
  local_1b8[11] = 0x30;
  local_1b8[12] = 0x3c;
  local_1b8[13] = 0xc;
  local_1b8[14] = 0x31;
  local_1b8[15] = 0x21;
  local_1b8[16] = 0x1e;
  local_1b8[17] = 0x3d;
  local_1b8[18] = 0x24;
  local_1b8[19] = 0x27;
  local_1b8[20] = 0x38;
  local_1b8[21] = 0x2c;
  local_1b8[22] = 0x35;
  local_1b8[23] = 0x10;
  local_1b8[24] = 0x37;
  local_1b8[25] = 0x33;
  local_1b8[26] = 0x3b;
  local_1b8[27] = 0x1b;
  local_1b8[28] = 0x29;
  local_1b8[29] = 0x3e;
  local_1b8[30] = 0x17;
  local_1b8[31] = 0x2a;
  local_1b8[32] = 0x2f;
  local_1b8[33] = 0x2b;
  local_1b8[34] = 0x15;
  local_1b8[35] = 0xe;
  local_1b8[36] = 0x18;
  local_1b8[37] = 0x43;
  local_118[0] = 0x5b;
  local_118[1] = 0x54;
  local_118[2] = 0x55;
  local_118[3] = 0x5c;
  local_118[4] = 0x59;
  local_118[5] = 0x6a;
  local_118[6] = 0x75;
  local_118[7] = 0x76;
  local_118[8] = 0x67;
  local_118[9] = 0x7a;
  local_118[10] = 0x1d;
  local_118[11] = 0x5e;
  local_118[12] = 5;
  local_118[13] = 0x7e;
  local_118[14] = 5;
  local_118[15] = 0x55;
  local_118[16] = 0x2b;
  local_118[17] = 0x62;
  local_118[18] = 0x4c;
  local_118[19] = 0x13;
  local_118[20] = 0x5b;
  local_118[21] = 0x47;
  local_118[22] = 6;
  local_118[23] = 0x62;
  local_118[24] = 0x5a;
  local_118[25] = 7;
  local_118[26] = 0x55;
  local_118[27] = 0x44;
  local_118[28] = 0x5e;
  local_118[29] = 0xd;
  local_118[30] = 0x7b;
  local_118[31] = 0x46;
  local_118[32] = 0x70;
  local_118[33] = 0x4f;
  local_118[34] = 0x25;
  local_118[35] = 0x60;
  local_118[36] = 0x2b;
  local_118[37] = 0x3e;
  local_1c0 = 0;
  do {
    if (0x25 < local_1c0) {
      fwrite("congrats, now go submit it\n",1,0x1b,stdout);
      uVar1 = 0;
LAB_00101579:
      if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
        __stack_chk_fail();
      }
      return uVar1;
    }
    if ((byte)((byte)local_118[local_1c0] ^ (byte)local_1b8[local_1c0]) != local_78[local_1c0]) {
      fwrite(&DAT_0010201f,1,4,stdout);
      uVar1 = 0x539;
      goto LAB_00101579;
    }
    local_1c0 = local_1c0 + 1;
  } while( true );
}
```

- We can see that it's making a XOR between the input and another string char by char, the output is verified with another char from another string which can be the flag.
- As we know ```A XOR B = C``` and to get the original flag we can use ```C XOR B = A```.
- Let's make a script to do that.

```python
local_1b8 = [0] * 38
local_1b8[0] = 0x12
local_1b8[1] = 0x3a
local_1b8[2] = 0x32
local_1b8[3] = 0x39
local_1b8[4] = 0x11
local_1b8[5] = 0xb
local_1b8[6] = 0x16
local_1b8[7] = 0x1d
local_1b8[8] = 0x1c
local_1b8[9] = 0x19
local_1b8[10] = 0x2d
local_1b8[11] = 0x30
local_1b8[12] = 0x3c
local_1b8[13] = 0xc
local_1b8[14] = 0x31
local_1b8[15] = 0x21
local_1b8[16] = 0x1e
local_1b8[17] = 0x3d
local_1b8[18] = 0x24
local_1b8[19] = 0x27
local_1b8[20] = 0x38
local_1b8[21] = 0x2c
local_1b8[22] = 0x35
local_1b8[23] = 0x10
local_1b8[24] = 0x37
local_1b8[25] = 0x33
local_1b8[26] = 0x3b
local_1b8[27] = 0x1b
local_1b8[28] = 0x29
local_1b8[29] = 0x3e
local_1b8[30] = 0x17
local_1b8[31] = 0x2a
local_1b8[32] = 0x2f
local_1b8[33] = 0x2b
local_1b8[34] = 0x15
local_1b8[35] = 0xe
local_1b8[36] = 0x18
local_1b8[37] = 0x43

local_118 = [0] * 38
local_118[0] = 0x5b
local_118[1] = 0x54
local_118[2] = 0x55
local_118[3] = 0x5c
local_118[4] = 0x59
local_118[5] = 0x6a
local_118[6] = 0x75
local_118[7] = 0x76
local_118[8] = 0x67
local_118[9] = 0x7a
local_118[10] = 0x1d
local_118[11] = 0x5e
local_118[12] = 5
local_118[13] = 0x7e
local_118[14] = 5
local_118[15] = 0x55
local_118[16] = 0x2b
local_118[17] = 0x62
local_118[18] = 0x4c
local_118[19] = 0x13
local_118[20] = 0x5b
local_118[21] = 0x47
local_118[22] = 6
local_118[23] = 0x62
local_118[24] = 0x5a
local_118[25] = 7
local_118[26] = 0x55
local_118[27] = 0x44
local_118[28] = 0x5e
local_118[29] = 0xd
local_118[30] = 0x7b
local_118[31] = 0x46
local_118[32] = 0x70
local_118[33] = 0x4f
local_118[34] = 0x25
local_118[35] = 0x60
local_118[36] = 0x2b
local_118[37] = 0x3e

input1 = ""

for i in local_1b8:
    c1 = str(hex(i)).replace("0x", "")
    if len(c1) == 2:
        input1 += c1
    else:
        input1 += "0"
        input1 += c1

input2 = ""

for j in local_118:
    c2 = str(hex(j)).replace("0x", "")
    if len(c2) == 2:
        input2 += c2
    else:
        input2 += "0"
        input2 += c2

output_hex = str(hex(int(input1, 16) ^ int(input2, 16))).replace("0x", "")

output = str(bytearray.fromhex(output_hex).decode())

print(output)
```

- The output: ```IngeHack{c0n9r4t5_h4ck3rm4n_w3ll_d0n3}```