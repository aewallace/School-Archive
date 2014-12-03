//
//  BIDAppDelegate.h
//  RPNCalc
//
//  Created by Richard Chapman on 9/12/12.
//  Copyright (c) 2012 Auburn University. All rights reserved.
//
//  used by Albert Wallace on 15 June 2013, for COMP4970
//

#import <UIKit/UIKit.h>

@class BIDViewController;

@interface BIDAppDelegate : UIResponder <UIApplicationDelegate>

@property (strong, nonatomic) UIWindow *window;

@property (strong, nonatomic) BIDViewController *viewController;

@end
