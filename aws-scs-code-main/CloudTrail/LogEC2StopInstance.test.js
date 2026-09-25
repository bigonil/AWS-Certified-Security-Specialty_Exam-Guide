const { handler } = require('./LogEC2StopInstance');

describe('LogEC2StopInstance Handler', () => {
    it('should call the callback with "Finished"', () => {
        const mockEvent = { detail: { 'instance-id': 'i-1234567890abcdef0' } };
        const mockContext = {};
        const mockCallback = jest.fn();

        handler(mockEvent, mockContext, mockCallback);

        expect(mockCallback).toHaveBeenCalledTimes(1);
        expect(mockCallback).toHaveBeenCalledWith(null, 'Finished');
    });

    it('should log the event', () => {
        const mockEvent = { test: 'event' };
        const mockContext = {};
        const mockCallback = jest.fn();

        const consoleSpy = jest.spyOn(console, 'log').mockImplementation();

        handler(mockEvent, mockContext, mockCallback);

        expect(consoleSpy).toHaveBeenCalledWith('LogEC2StopInstance');
        expect(consoleSpy).toHaveBeenCalledWith('Received event:', JSON.stringify(mockEvent, null, 2));

        consoleSpy.mockRestore();
    });
});
