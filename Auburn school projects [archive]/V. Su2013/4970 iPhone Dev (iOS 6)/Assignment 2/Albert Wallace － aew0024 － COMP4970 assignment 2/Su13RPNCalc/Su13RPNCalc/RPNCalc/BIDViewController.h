//
//  BIDViewController.h
//  RPNCalc
//
//  Created by Richard Chapman on 9/12/12.
//  Copyright (c) 2012 Auburn University. All rights reserved.
//
//  tweaked by Albert Wallace on 15 June 2013, for COMP4970
//

#import <UIKit/UIKit.h>

@interface BIDViewController : UIViewController
@property (strong, nonatomic) IBOutletCollection(UILabel) NSArray *calcDisplay;

@property (strong, nonatomic) IBOutlet UIView *calcDisplayLS;
@property (strong, nonatomic) IBOutlet UIView *calcDisplayPortrait;
@property (nonatomic) float display;
@property (nonatomic) NSString *displayString;
@property (nonatomic) float x;
@property (nonatomic) float y;
@property (nonatomic) float z;
@property (nonatomic) bool displayEntered;
@property (nonatomic) bool clearDisplayOnNumber;

- (IBAction)keyEnter:(id)sender;
- (IBAction)keyClr:(id)sender;
- (IBAction)keyPop:(id)sender;
- (IBAction)keyPlus:(id)sender;
- (IBAction)key7:(id)sender;
- (IBAction)key8:(id)sender;
- (IBAction)key9:(id)sender;
- (IBAction)keyMinus:(id)sender;
- (IBAction)key4:(id)sender;
- (IBAction)key5:(id)sender;
- (IBAction)key6:(id)sender;
- (IBAction)keyMult:(id)sender;
- (IBAction)key1:(id)sender;
- (IBAction)key2:(id)sender;
- (IBAction)key3:(id)sender;
- (IBAction)keyDiv:(id)sender;
- (IBAction)keyDecimal:(id)sender;
- (IBAction)key0:(id)sender;
- (IBAction)keyChs:(id)sender;
- (IBAction)keyExp:(id)sender;
- (IBAction)keyInv:(id)sender;
- (IBAction)keySqrt:(id)sender;
- (IBAction)keySq:(id)sender;

- (void) updateDisplay;
- (void) numberKey:(NSString *)number;
- (void) displayResult:(float) result;
- (void) push;
- (void) pop;
@end
