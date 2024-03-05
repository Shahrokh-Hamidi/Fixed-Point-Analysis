/*
 Created by Shahrokh Hamidi
 PhD., Electrical & Computer Engineering
 Waterloo, ON., Canada
*/


#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;



extern "C"{


int32_t DoubleTofixed(float d, int dp){

    return int32_t( d * float(1 << dp) + (d >=0 ? 0.5 : -0.5));

}


float FixedToDouble(int a, int dp){

    return float(a) / float(1 << dp);
}


int32_t* quantization(double *input, int len, int dp){
    
    
    int32_t *arr = (int32_t *) malloc(len * sizeof(int));

    for (int i = 0 ; i < len ; i ++){
        arr[i] = DoubleTofixed(input[i], dp);
    };
    return arr;

}


void free_memory(int *arr){

    free(arr);
    
}


}