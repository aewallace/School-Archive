//
//  BIDViewController.m
//  RPNCalc
//
//  Created by Richard Chapman on 9/12/12.
//  Copyright (c) 2012 Auburn University. All rights reserved.
//
//  tweaked by Albert Wallace on 15 June 2013, for COMP4970
//

#import "BIDViewController.h"
#import "math.h"

//used for additional rotation capability
#define degreesToRadians(x) (M_PI * (x) / 180.0)

@interface BIDViewController ()

@end

//outlets
@implementation BIDViewController
@synthesize calcDisplay;
@synthesize calcDisplayLS;
@synthesize calcDisplayPortrait;


// float value of the number in the display
@synthesize display;
// string of the number in the display
@synthesize displayString;
// true => the string in displayString is on the stack as a float
@synthesize displayEntered;
// when a number key is pressed, should the display be cleared or the number appended
@synthesize clearDisplayOnNumber;
// floats for the stack values, x = top of stack, y = middle, z = bottom of stack
@synthesize x;
@synthesize y;
@synthesize z;

// move displayString into the display label
- (void) updateDisplay {
    [[calcDisplay objectAtIndex:0] setText: displayString];
    [[calcDisplay objectAtIndex:1] setText: displayString];
    
}

//all the following added to support rotation
- (void)willAnimateRotationToInterfaceOrientation:(UIInterfaceOrientation)toInterfaceOrientation duration:(NSTimeInterval)duration{
    
    if (toInterfaceOrientation == UIInterfaceOrientationPortrait){
        self.view = self.calcDisplayPortrait;
        self.view.transform = CGAffineTransformIdentity;
        self.view.transform = CGAffineTransformMakeRotation(degreesToRadians(0));
        self.view.bounds = CGRectMake(0.0, 0.0, 320.0, 460.0);
    }
    if (toInterfaceOrientation == UIInterfaceOrientationLandscapeLeft){
        self.view = self.calcDisplayLS;
        self.view.transform = CGAffineTransformIdentity;
        self.view.transform = CGAffineTransformMakeRotation(degreesToRadians(-90));
        self.view.bounds = CGRectMake(0.0, 0.0, 480.0, 300.0);
    }
    if (toInterfaceOrientation == UIInterfaceOrientationLandscapeRight){
        self.view = self.calcDisplayLS;
        self.view.transform = CGAffineTransformIdentity;
        self.view.transform = CGAffineTransformMakeRotation(degreesToRadians(90));
        self.view.bounds = CGRectMake(0.0, 0.0, 480.0, 300.0);
    }

} //end rotation support

// if  number key was pressed, if it is not the first digit of a new nember being entered,
// append to the displayString, else clear the displayString and 
- (void) numberKey:(NSString *)number {
    if (!clearDisplayOnNumber) {
        displayString = [displayString stringByAppendingString:number];
        [self updateDisplay];
    } else {
        clearDisplayOnNumber = FALSE;
        //[self push];
        displayString = number;
        [self updateDisplay];
        displayEntered = FALSE;
    }

}

// display the argument value result in the display
- (void)displayResult:(float)result {
    display = result;
    displayEntered = TRUE;
    if (display != INFINITY) { 
        displayString = [[NSString alloc] initWithFormat:@"%f",display];
       
    } else {
        displayString = @"OVERFLOW";
    }    
    [self updateDisplay];
    clearDisplayOnNumber = TRUE;
}


// push down the values in the stack, throwing away bottom value 
- (void) push{
    z = y;
    y = x;
    x = display;
    
}

// pop values up the stack, replicating bottom value 
- (void) pop {
    display = x;
    x = y;
    y = z;
}


- (void) checkDisplay {
    if (!displayEntered) {
        display = [displayString floatValue];
        displayEntered = TRUE;
    }
}

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    x = 0.0;
    y = 0.0;
    z = 0.0;
    display = 0.0;
    displayString = @"0.0";
    displayEntered = TRUE;
    clearDisplayOnNumber = TRUE;
    //[self updateDisplay];
}

- (void)viewDidUnload
{
    [self setCalcDisplay:nil];
    [self setCalcDisplayLS:nil];
    [self setCalcDisplayPortrait:nil];
    [super viewDidUnload];
    // Release any retained subviews of the main view.
    displayString = nil;
}


// Action methods, one per key 
- (IBAction)keyEnter:(id)sender {
    // convert string in display to float, display it
    [self displayResult:[displayString floatValue] ];
    [self push];

}

- (IBAction)keyClr:(id)sender {
    // change display to 0.0
    [self displayResult:0.0];
}

- (IBAction)keyPop:(id)sender {
    // pop and display result 
    [self pop];
    [self displayResult: display];
}

- (IBAction)keyPlus:(id)sender {
    [self checkDisplay];
    float arg1 = x;
    float arg2 = display;
    [self pop];
    //[self pop];
    [self displayResult: arg1 + arg2];

}

- (IBAction)keyMinus:(id)sender {
    [self checkDisplay];
    float arg1 = x;
    float arg2 = display;
    [self pop];
    //[self pop];
    [self displayResult: arg1 - arg2];

}

- (IBAction)keyMult:(id)sender {
    [self checkDisplay];
    float arg1 = x;
    float arg2 = display;
    [self pop];
    //[self pop];
    [self displayResult: arg1  * arg2];


}

- (IBAction)keyDiv:(id)sender {
    [self checkDisplay];
    float arg1 = x;
    float arg2 = display;
    [self pop];
    //[self pop];
    if (arg2 != 0) {
        [self displayResult: arg1 / arg2];
    } else {
        displayString = @"DIV BY 0";
        [self updateDisplay];
    }
}

- (IBAction)keyExp:(id)sender {
    [self checkDisplay];
    float arg1 = x;
    float arg2 = display;
    [self pop];
    //[self pop];
    display = pow(arg1,arg2);
    [self displayResult:display];
    
}

- (IBAction)key7:(id)sender {
    [self numberKey:@"7"];
  }

- (IBAction)key8:(id)sender {
    [self numberKey:@"8"];
}

- (IBAction)key9:(id)sender {
    [self numberKey:@"9"];
}



- (IBAction)key4:(id)sender {
    [self numberKey:@"4"];

}

- (IBAction)key5:(id)sender {
    [self numberKey:@"5"];

}

- (IBAction)key6:(id)sender {
    [self numberKey:@"6"];

}


- (IBAction)key1:(id)sender {
    [self numberKey:@"1"];

}

- (IBAction)key2:(id)sender {
    [self numberKey:@"2"];

}

- (IBAction)key3:(id)sender {
    [self numberKey:@"3"];

}


- (IBAction)keyDecimal:(id)sender {
    [self numberKey:@"."];
}

- (IBAction)key0:(id)sender {
    [self numberKey:@"0"];

}

- (IBAction)keyChs:(id)sender {
    // different if entered or not
    if (displayEntered) { 
        display = - display;
        [self displayResult:display];
    } else {
        // prepend a minus or remove it
        if([displayString rangeOfString:@"-"].location != NSNotFound) {
            // found it, remove it
            displayString = [displayString substringFromIndex:1];
        } else {
            // it's not there, prepend it
            NSString *s1 = @"-";
            displayString = [s1 stringByAppendingString:displayString];
        
        }
    [self updateDisplay];
    }
}



- (IBAction)keyInv:(id)sender {
    [self checkDisplay];
    display = 1/display;
    [self displayResult:display];
    
}

- (IBAction)keySqrt:(id)sender {
    [self checkDisplay];
    display = sqrt(display);
    [self displayResult:display];
    
}

- (IBAction)keySq:(id)sender {
    [self checkDisplay];
    display = display*display;
    [self displayResult:display];
    
}


@end
